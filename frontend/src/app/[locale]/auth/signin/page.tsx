import * as React from 'react'


import { Title } from '@/components/global/title'
import { Description } from '@/components/global/description'
import { SignInWith } from '@/components/auth/signin-with'
import { TextLink } from '@/components/global/text-link'
import { ButtonLink } from '@/components/global/button-link'
import { SignInForm } from './signin-form'
import { MyLogo } from '@/components/global/logo'
import { useTranslations } from 'next-intl'

export default function SignInPage() {
  const t = useTranslations('auth.signin')
  return (
    <div className="container flex min-h-screen w-screen flex-col items-center justify-center py-8">
      <ButtonLink
        href="/"
        className="absolute left-4 top-4 md:left-8 md:top-8"
        startIconName="ChevronLeft"
        translate="yes"
      >
        home
      </ButtonLink>
      <div className="mx-auto flex w-full max-w-[320px] flex-col justify-center space-y-6">
        <div className="flex flex-col space-y-2 text-center">
          <MyLogo className="mx-auto size-12 min-w-12" />
          <Title translate="yes">{'auth.signin.title'}</Title>
        </div>
        <div className="grid gap-6">
          <SignInForm />
          <SignInWith />
        </div>
        <div className="flex items-center justify-between text-sm">
          <TextLink
            href="/auth/signup"
            className="underline hover:no-underline"
            translate="yes"
          >
            {'auth.signin.no_account'}
          </TextLink>
        </div>
      </div>
    </div>
  )
}
