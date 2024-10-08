'use client'

import * as React from 'react'
import { SWRConfig } from 'swr'
import { fetcher } from '@/lib/utils/fetcher'


const SWRProvider = ({ children }: { children?: React.ReactNode }) => {
  return <SWRConfig value={{ fetcher }}>{children}</SWRConfig>
}

export { SWRProvider }
