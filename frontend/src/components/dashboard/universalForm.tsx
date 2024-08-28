"use client";
import { FC, useEffect } from "react";
import { useForm, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useTranslations } from "next-intl";
import { useProfile } from "@/hooks/useProfile";
import { useSubmitForm } from "@/hooks/useSubmitForm";
import { useFetchData } from "@/hooks/useFetchData";
import LoadingPage from "@/components/global/loading-page";
import AlertDestructive from "@/components/global/error-page";
import { entityConfigMap } from "@/config/entities";
import { EntityConfigMap, BaseEntityConfig } from "@/types/base.d";

interface UniversalFormProps {
  entity: keyof EntityConfigMap; // entityConfigMap의 키로 타입 제한
  id?: string;
}

const UniversalForm: FC<UniversalFormProps> = ({ entity, id }) => {
  const isEdit = Boolean(id);
  const t = useTranslations();
  const config: BaseEntityConfig = entityConfigMap[entity]; // 해당 엔티티의 config 가져오기

  // formSchema는 config에서 동적으로 가져옴
  const form = useForm({
    resolver: zodResolver(config.schema),
    defaultValues: {}, // 기본값을 빈 객체로 설정
  });

  const { submitForm, error: submitError } = useSubmitForm(
    `${process.env.NEXT_PUBLIC_API_URL}/${entity}/`,
    `/dashboard/${entity}`
  );

  const { profile, loading: profileLoading, error: profileError } = useProfile();
  const { data, loading, error } = useFetchData(
    id ? `${process.env.NEXT_PUBLIC_API_URL}/${entity}/${id}` : ""
  );

  useEffect(() => {
    if (data) {
      // data가 객체인지 확인
      if (typeof data !== "object" || data === null) {
        console.error("Invalid data received", data);
        return;
      }
      form.reset(data); // 데이터가 있을 경우 폼을 초기화
    }
  }, [data, form]);

  if (loading || profileLoading) return <LoadingPage />;
  if (error || profileError) return <AlertDestructive error={error || profileError} />;

  const onSubmit = (data: any) => {
    submitForm({
      ...data,
      profile_id: profile?.profile_id, // 프로필 ID 추가
    });
  };

  return (
    <>
      <h1 className="text-3xl pt-2 font-bold text-primary">
        {isEdit ? t(`forms.${entity}.save_changes`) : t(`form.${entity}.create_new`)}
      </h1>
      <div className="flex flex-col gap-2 mt-10">
        <Card>
          <CardHeader>
            <CardTitle>
              {isEdit ? t(`forms.${entity}.save_changes`) : t(`forms.${entity}.create_new`)}
            </CardTitle>
          </CardHeader>
          <CardContent>
            <Form {...form}>
              <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
                {Object.keys(config.fields).map((fieldName) => {
                  const fieldData = config.fields[fieldName];

                  // 폼에 표시할 필드만 렌더링
                  if (!fieldData.showInForm) return null;

                  if (Array.isArray(fieldData.options)) {
                    return (
                      <FormField
                        key={fieldName}
                        control={form.control}
                        name={fieldName}
                        render={({ field }) => (
                          <FormItem>
                            <FormLabel>{t(`forms.${entity}.${fieldName}`)}</FormLabel>
                            <FormControl>
                              <Controller
                                name={fieldName}
                                control={form.control}
                                render={({ field }) => (
                                  <Select
                                    onValueChange={field.onChange}
                                    value={field.value || fieldData.options[0]}
                                    defaultValue={field.value || fieldData.options[0]}
                                  >
                                    <SelectTrigger>
                                      <SelectValue placeholder={t(`forms.${entity}.${fieldName}`)} />
                                    </SelectTrigger>
                                    <SelectContent>
                                      {fieldData.options.map((option: string) => (
                                        <SelectItem key={option} value={option}>
                                          {t(`common.fields.${option}`)}
                                        </SelectItem>
                                      ))}
                                    </SelectContent>
                                  </Select>
                                )}
                              />
                            </FormControl>
                            <FormMessage />
                          </FormItem>
                        )}
                      />
                    );
                  }

                  return (
                    <FormField
                      key={fieldName}
                      control={form.control}
                      name={fieldName}
                      render={({ field }) => (
                        <FormItem>
                          <FormLabel>{t(`forms.${entity}.${fieldName}`)}</FormLabel>
                          <FormControl>
                            <Input
                              placeholder={t(`forms.${entity}.${fieldName}`)}
                              {...field}
                              disabled={
                                typeof fieldData.disabled === "function"
                                  ? fieldData.disabled(id)
                                  : fieldData.disabled
                              }
                            />
                          </FormControl>
                          <FormMessage />
                        </FormItem>
                      )}
                    />
                  );
                })}
                <Button type="submit" className="w-full">
                  {isEdit ? t("common.actions.save_changes") : t("common.actions.create")}
                </Button>
              </form>
            </Form>
          </CardContent>
        </Card>
      </div>
    </>
  );
};

export default UniversalForm;
