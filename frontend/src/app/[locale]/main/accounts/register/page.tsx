// app/[locale]/dashboard/accounts/[id]/page.tsx

'use client'
import React from 'react'
import UniversalForm from '@/components/dashboard/universalForm'

export default function CreateNewAccount() {
  return (
    <div>
        <UniversalForm entity="accounts" />
    </div>
  )
}
