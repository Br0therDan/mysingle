"use client";
import { ColumnDef } from "@tanstack/react-table";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { MoreHorizontal } from "lucide-react";
import { formatInTimeZone } from "date-fns-tz";
import Link from "next/link";

export type Account = {
  account_id: string;
  account_name: string;
  account_type: string;
  onwer: string;
  created_at: string; // 이 부분을 수정해야 합니다.
  updated_at: string; // 이 부분을 수정해야 합니다.
};

export const columns: ColumnDef<Account>[] = [
  {
    accessorKey: "account_name",
    header: "account_name",
    cell: ({ row }) => {
      const accountId = row.original.account_id; // account_id 가져오기
      return (
        <Link
          href={`/accounts/${accountId}`}
          className="text-blue-600 hover:underline"
        >
          {row.getValue("account_name")}
        </Link>
      );
    },
  },
  {
    accessorKey: "account_type",
    header: "account_type",
  },
  {
    accessorKey: "owner",
    header: "owner",
  },
  {
    accessorKey: "created_at",
    header: "created_at",
    cell: ({ getValue }) => {
      const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
      const date = new Date(getValue() as string);
      return formatInTimeZone(date, userTimeZone, "yyyy-MM-dd HH:mm");
    },
  },
  {
    accessorKey: "updated_at",
    header: "updated_at",
    cell: ({ getValue }) => {
      const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
      const date = new Date(getValue() as string);
      return formatInTimeZone(date, userTimeZone, "yyyy-MM-dd HH:mm");
    },
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const account_data = row.original;
      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only"></span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuSeparator />
            <DropdownMenuItem>Detail</DropdownMenuItem>
            <DropdownMenuItem>Edit</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];
