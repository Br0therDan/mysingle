import { useState } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";
import { useTranslations } from "next-intl";

// 커스텀 훅 정의
export const useSubmitForm = (apiUrl: string, successRedirectUrl: string) => {
  const [error, setError] = useState<string | null>(null);
  const t = useTranslations();
  const router = useRouter();

  const submitForm = async (formData: any) => {
    try {
      const { accessToken } = await fetch("/api/v1/token").then((res) =>
        res.json()
      );
      await axios.post(apiUrl, formData, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      router.push(successRedirectUrl);
    } catch (err) {
      setError(t("AlertMessages.update_error")); // 에러 처리
    }
  };

  return { submitForm, error };
};