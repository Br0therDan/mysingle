import * as React from 'react'
import Link from 'next/link'


import { SiteLogo } from '@/components/global/site-logo'
import { siteConfig } from '@/config/site'
import { absoluteUrl } from '@/lib/utils/url'

const MobileNavigation = () => {
  return (
    <div className="grid w-full max-w-md gap-4">
      <div className="flex items-center gap-4">
        <SiteLogo className="size-8 min-w-8" />
        <span>{siteConfig?.title}</span>
      </div>
      <nav className="grid gap-2 text-sm">
        <Link href={absoluteUrl('/')} className="hover:underline">
          Home
        </Link>
        <Link href={absoluteUrl('/posts')} className="hover:underline">
          Posts
        </Link>
      </nav>
    </div>
  )
}

export { MobileNavigation }
