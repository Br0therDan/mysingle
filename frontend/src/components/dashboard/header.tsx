// src/components/dashboard/header.tsx
'use client'
import React from 'react'
import MobileSidebar from '@/components/dashboard/mobile-sidebar'
import SearchBar from './search-bar'
import { SiteBrand } from '../global/site-brand'
import { SignOutButton } from '../auth/signout-button'
import { AccountMenu } from '../global/account-menu'


export default function Header() {
  return (
    <header className="sticky top-0 z-30 flex h-14 items-center gap-4 px-4 bg-slate-100 sm:static sm:px-6">
      <MobileSidebar />
      <div className="flex w-full items-center justify-between gap-3">
        <div className="hidden sm:flex">
          <SiteBrand />
        </div>
        <SearchBar />
        <AccountMenu />
        {/* <Auth0UserButton /> */}
      </div>
    </header>
  )
}
