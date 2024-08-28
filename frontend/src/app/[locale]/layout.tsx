import { Inter as FontSans } from "next/font/google";
import "../globals.css";
import { getMessages, getTranslations, unstable_setRequestLocale } from "next-intl/server";
import { NextIntlClientProvider } from "next-intl";
import { AppProvider } from '@/context/app-provider';
import { cn } from '@/lib/utils';
import config from '@/config';
import { Metadata } from 'next';

const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
});

// TODO: Configuration 파일로 이동후 import
const locales = ['en', 'ko'];
 
export function generateStaticParams() {
  return locales.map((locale) => ({locale}));
}

export default async function LocaleLayout({
  children,
  params: { locale },
}: Readonly<{
  children: React.ReactNode;
  params: { locale: string };
}>) {
  const message = await getMessages();
  unstable_setRequestLocale(locale);
  return (
    <html lang={locale}>
      <body
        className={cn(
          "min-h-screen bg-background font-sans antialiased",
          fontSans.variable
        )}
      >
        <AppProvider>
          <NextIntlClientProvider messages={message}>
            {children}
          </NextIntlClientProvider>
        </AppProvider>
      </body>
    </html>
  );
}


