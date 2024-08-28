"use client";  // 이 줄을 추가하여 클라이언트 컴포넌트로 설정합니다.

import BreadcrumbForm from '@/components/dashboard/breadcrumb';
import Header from "@/components/dashboard/header";
import Sidebar from "@/components/dashboard/sidebar";
import { RootState } from '@/store/store';
import { useEffect } from 'react';
import { useTranslations } from 'next-intl';
import { useDispatch, useSelector } from "react-redux";
import { useAuth } from '@/hooks/use-auth';


export default function DashboardLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const { user } = useAuth();
  const  t  = useTranslations();
  const title = `${user} 의${t('dashboard.title')}`
  const description = t('dashboard.description')

  useEffect(() => {
    document.title = t(title);
    document.querySelector('meta[name="description"]')?.setAttribute('content', description);
  },[title, description, t]);

  const isExpanded = useSelector((state: RootState) => state.sidebar.isExpanded);
  const dispatch = useDispatch();
  
  return (
      <div className="flex min-h-screen w-full flex-col bg-muted/40">
        <Header />
        <Sidebar />
        <div className={`flex flex-col pl-0 py-4 ${isExpanded ? "sm:pl-64" : "sm:pl-16"}`}>
          <main className="grid flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8">
            <BreadcrumbForm />
            {children}
          </main>
        </div>
      </div>
  );
}