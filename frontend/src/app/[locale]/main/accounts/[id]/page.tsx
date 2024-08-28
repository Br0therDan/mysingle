// app/[locale]/dashboard/accounts/[id]/page.tsx

'use client'
import React from 'react'
import { useParams } from "next/navigation";
import UniversalForm from '@/components/dashboard/universalForm';

export default function AccountDetail() {
  const params = useParams();
  const id = params.id as string; 
  return (
    <div>
      <UniversalForm entity="accounts" id={id}/>
    </div>
  )
}
