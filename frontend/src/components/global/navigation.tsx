'use client'

import * as React from 'react'
import Link from 'next/link'

import {
  NavigationMenuLink,
  // NavigationMenuTrigger,
  // NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuList,
  NavigationMenu,
} from '@/components/ui/navigation-menu'
import { absoluteUrl } from '@/lib/utils'

interface NavigationItem {
  id: number
  title: string
  href: string
}

const Items: NavigationItem = [
  {
    id: 1,
    title: 'Docs',
    href: '/docs',
  },
  {
    id: 2,
    title: 'About',
    href: '/about',
  },
]

const Navigation = () => {
  return (
    <NavigationMenu className="hidden md:flex">
      <NavigationMenuList className="gap-2">
        {Items.map((item) => (
          <NavigationMenuLink key={item.id} asChild>
            <Link href={item.href}>
              <NavigationMenuItem>{item.title}</NavigationMenuItem>
            </Link>
          </NavigationMenuLink>
        ))}
      </NavigationMenuList>
    </NavigationMenu>
  )
}

export { Navigation }
