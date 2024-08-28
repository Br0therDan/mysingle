'use client';

import React, { useEffect, useState } from 'react';
import { usePathname } from 'next/navigation';
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb';
import Link from 'next/link';
import { useTranslations } from 'next-intl';
import { breadcrumbMappings } from '@/config/base';

export default function BreadcrumbForm() {
  const t = useTranslations();
  const pathname = usePathname();
  const [breadcrumbs, setBreadcrumbs] = useState<{ href?: string; label: string }[]>([]);

  useEffect(() => {
    const pathSegments = pathname.split('/').filter(Boolean);

    // locale 부분 제거 (첫 번째 segment가 'en' 또는 'ko'라고 가정)
    const filteredSegments = pathSegments.length > 1 && (pathSegments[0] === 'en' || pathSegments[0] === 'ko')
      ? pathSegments.slice(1)
      : pathSegments;

    const breadcrumbList = filteredSegments.map((segment, index) => {
      const href = `/${filteredSegments.slice(0, index + 1).join('/')}`;
      const labelKey = breadcrumbMappings[href] || segment;
      const label = typeof labelKey === 'string' ? t(`breadcrumb.${labelKey}`, { defaultValue: labelKey }) : segment;

      return { href, label };
    });

    setBreadcrumbs([{ href: '/dashboard', label: t('breadcrumb.dashboard') }, ...breadcrumbList]);
  }, [pathname, t]);

  return (
    <div className='px-4 hidden sm:px-6 md:flex'>
      <Breadcrumb>
        <BreadcrumbList>
          {breadcrumbs.map((item, index) => (
            <React.Fragment key={index}>
              <BreadcrumbItem>
                {item.href ? (
                  <BreadcrumbLink>
                    <Link href={item.href}>{item.label}</Link>
                  </BreadcrumbLink>
                ) : (
                  <BreadcrumbPage className="max-w-20 truncate md:max-w-none">
                    {item.label}
                  </BreadcrumbPage>
                )}
              </BreadcrumbItem>
              {index < breadcrumbs.length - 1 && <BreadcrumbSeparator />}
            </React.Fragment>
          ))}
        </BreadcrumbList>
      </Breadcrumb>
    </div>
  );
}
