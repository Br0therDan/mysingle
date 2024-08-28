import * as React from 'react'


import { Title } from '@/components/global/title'
import { Description } from '@/components/global/description'
import { TextLink } from '@/components/global/text-link'
import { ButtonLink } from '@/components/global/button-link'


import { SignUpForm } from './signup-form'
import { Policy } from './policy'
import { MyLogo } from '@/components/global/logo'
import { useTranslations } from 'next-intl'

export default function SignUpPage() {
  const t = useTranslations()
  return (
    <div className="container flex min-h-screen w-screen flex-col items-center justify-center py-8">
      <ButtonLink
        href="/auth/signin"
        className="absolute right-4 top-4 md:right-8 md:top-8"
        translate="yes"
      >
        signin
      </ButtonLink>
      <div className="mx-auto flex w-full max-w-[320px] flex-col justify-center space-y-6">
        <div className="flex flex-col space-y-2 text-center">
          <MyLogo className="mx-auto size-12 min-w-12" />
          <Title translate='yes'>{'auth.signup.title'}</Title>
        </div>
        <div className="grid gap-6">
          <SignUpForm />
          <Policy />
        </div>
        <div className="flex items-center justify-between text-sm">
          <TextLink
            href="/auth/signin"
            className="underline hover:no-underline"
            translate="yes"
          >
            {'auth.signup.already_have_account'}
          </TextLink>
        </div>
      </div>
    </div>
  )
}
