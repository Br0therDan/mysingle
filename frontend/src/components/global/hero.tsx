"use client";

import * as React from "react";
import Link from "next/link";
import { useTranslations } from "next-intl";
import { buttonVariants } from "@/components/ui/button";
import { LucideIcon } from "@/lib/lucide-icon";
import { siteConfig } from "@/config/site";
import { cn } from '@/lib/utils';

const Hero = () => {
  const t = useTranslations();

  return (
    <section className="w-full py-12 md:py-24">
      <div className="container px-4 md:px-6">
        <div className="flex flex-col items-center space-y-4 text-center">
          <div className="space-y-2">
            <h1 className="text-3xl font-semibold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
              {t('site.title')}
            </h1>
            <p className="mx-auto max-w-[640px] text-gray-500 dark:text-gray-400 md:text-xl">
              {t('site.description')}
            </p>
          </div>
          <div className="space-x-4">
            <Link
              className={cn(buttonVariants({ variant: "default" }))}
              href="/posts"
            >
              {t("site.button.get_started")}
            </Link>
            <Link
              className={cn(buttonVariants({ variant: "outline" }))}
              href="https://github.com/w3labkr/nextjs-supabase-dashboard"
              target="_blank"
            >
              {t("github")}
              <LucideIcon
                name="ExternalLink"
                className="-mt-0.5 ml-1 size-3.5 min-w-3.5"
              />
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export { Hero };
