"use client";

import * as React from "react";
import { useTranslations } from "next-intl";

import { cn } from "@/lib/utils";

interface DescriptionProps extends React.HTMLAttributes<HTMLParagraphElement> {
  text?: string;
  ns?: string;
}

const Description = ({
  children,
  className,
  translate,
  text,
  ns,
  ...props
}: DescriptionProps) => {
  const t = useTranslations();

  return (
    <p className={cn("text-sm text-muted-foreground", className)} {...props}>
      {text && translate === "yes" ? t(text, { ns }) : text}
      {children && typeof children === "string" && translate === "yes"
        ? t(children, { ns })
        : children}
    </p>
  );
};

export { Description, type DescriptionProps };
