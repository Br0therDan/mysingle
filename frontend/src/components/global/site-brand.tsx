import * as React from 'react'
import Link from 'next/link'

import { absoluteUrl } from '@/lib/utils'
import { siteConfig } from '@/config/site'
import { MyLogo } from './logo'

interface SiteBrandProps {
  className?: string
}

const SiteBrand = ({ className }: SiteBrandProps) => {
  return (
    <Link className={className} href={absoluteUrl('/main')}>
      <MyLogo className="size-10 min-w-10" />
      <span className="sr-only">{siteConfig?.name}</span>
    </Link>
  )
}

export { SiteBrand, type SiteBrandProps }
