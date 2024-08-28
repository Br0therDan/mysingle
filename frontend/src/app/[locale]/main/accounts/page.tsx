// src/dashboard/accounts/page.tsx

'use client'

import { useFetchData } from '@/hooks/useFetchData'
import { Account } from '@/types/base'
import DataTable from '@/components/dashboard/table/dataTable'
import { generateColumns } from '@/components/dashboard/table/generateColumn'
import LoadingPage from '@/components/global/loading-page'
import AlertDestructive from '@/components/global/error-page'

const AccountsPage = () => {
  const { data, loading, error } = useFetchData<Account[]>(
    `${process.env.NEXT_PUBLIC_API_URL}/accounts`
  )

  const columns = generateColumns<Account>('accounts')

  if (loading) return <LoadingPage />
  if (error) return <AlertDestructive message={error} />

  return (
    <div className="flex flex-1 flex-col gap-2 p-4">
      <h1 className="mb-4 text-2xl font-bold">Accounts</h1>
      {data && <DataTable columns={columns} data={data} title="accounts" />}
    </div>
  )
}

export default AccountsPage
