import * as React from 'react'
import { Title } from '@/components/global/title'
import { Description } from '@/components/global/description'
import { TextLink } from '@/components/global/text-link'
import { ButtonLink } from '@/components/global/button-link'
import { ForgotPasswordForm } from './forgot-password-form'
import { MyLogo } from '@/components/global/logo'

export default function ForgotPasswordPage() {
  return (
    <div className="container flex min-h-screen w-screen flex-col items-center justify-center py-8">
      <ButtonLink
        href="/auth/signin"
        className="absolute left-4 top-4 md:left-8 md:top-8"
        startIconName="ChevronLeft"
        translate="yes"
      >
        signin
      </ButtonLink>
      <div className="mx-auto flex w-full max-w-[320px] flex-col justify-center space-y-6">
        <div className="flex flex-col space-y-2 text-center">
          <MyLogo className="mx-auto size-12 min-w-12" />
          <Title translate="yes">forgot_your_password</Title>
          <Description translate="yes">
            enter_your_email_address_below_and_we_will_send_you_a_message_to_reset_your_password
          </Description>
        </div>
        <div className="grid gap-6">
          <ForgotPasswordForm />
        </div>
        <div className="flex items-center justify-between text-sm">
          <TextLink
            href="/auth/signup"
            className="underline hover:no-underline"
            translate="yes"
          >
            dont_have_an_account_sign_up
          </TextLink>
        </div>
      </div>
    </div>
  )
}
