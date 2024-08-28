'use client';
import React from "react";
import Link from "next/link";
import { Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { sideBarMenuItems } from '@/config/base';
import { useTranslations } from 'next-intl';
import Logo, { LogoDark } from '../global/logo';

// 타입 선언
interface SideBarMenuItem {
  title: string;
  href: string;
  icon: React.ComponentType<any>;
}

export default function MobileSidebar() {
  const t  = useTranslations(); // i18n 훅 사용
  const items: SideBarMenuItem[] = sideBarMenuItems(t); // `sideBarMenuItems` 함수 호출하여 배열로 변환

  return (
    <Sheet>
      <SheetTrigger asChild>
        <Menu className="h-6 w-6 z-0 font-bold text-gray-300 hover:text-white hover:font-bold sm:hidden" />
      </SheetTrigger>
      <SheetContent side="left" className="w-64 p-0 border-black text-white">
        <div className='flex top-0 z-30 h-16 items-center px-4 bg-black'>
          <LogoDark />
        </div>
        <nav className="flex flex-col gap-2 px-2 pt-5">
          {items.map((item: SideBarMenuItem) => (
            <Link
              key={item.title}
              href={item.href}
              className="flex h-9 text-sm text-black transition-colors hover:text-blue-600"
            >
              <div className="flex pl-3 gap-3">
                <item.icon className="h-5 w-5" />
                <span>{t(item.title)}</span> {/* 다국어 지원 적용 */}
              </div>
            </Link>
          ))}
        </nav>
      </SheetContent>
    </Sheet>
  );
}