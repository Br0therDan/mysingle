"use client";

import * as React from "react";
import { useSearchParams } from "next/navigation";
import { toast } from "sonner";
import { RiKakaoTalkFill } from "react-icons/ri";
import { Button, ButtonProps } from "@/components/ui/button";
import { useTranslations } from "next-intl";
import { createClient } from "@/utils/supabase/client";

interface SignInWithKakaoProps
  extends ButtonProps,
    Omit<React.ButtonHTMLAttributes<HTMLButtonElement>, "onClick"> {}

const SignInWithKakao = ({
  variant = "outline",
  ...props
}: SignInWithKakaoProps) => {
  const t = useTranslations();
  const searchParams = useSearchParams();

  const onClick = async () => {
    try {
      // if "next" is in param, use it as the redirect URL
      const next = (searchParams.get("next") as string) ?? "/main/dashboard";

      const supabase = createClient();
      const signed = await supabase.auth.signInWithOAuth({
        provider: "kakao",
        options: {
          // A URL to send the user to after they are confirmed.
          // Don't forget to change the URL in supabase's email template.
          redirectTo:
            process.env.NEXT_PUBLIC_SITE_URL +
            `/api/auth/callback?next=${next}`,
        },
      });

      if (signed?.error) throw new Error(signed?.error?.message);
    } catch (e: unknown) {
      toast.error((e as Error)?.message);
    }
  };

  return (
    <Button type="button" variant={variant} onClick={onClick} className='bg-yellow-300' {...props}>
      <RiKakaoTalkFill className="mr-2 h-5 w-5" />
      {t("auth.social.kakao")}
    </Button>
  );
};

export { SignInWithKakao, type SignInWithKakaoProps };
