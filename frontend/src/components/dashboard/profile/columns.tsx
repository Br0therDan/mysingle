// @/components/dashboard/profile/columns

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
import { ArrowUpDown, MoreHorizontal } from "lucide-react";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Org = {
  id: string;
  name: string;
  owner: string;
  description: string;
};

export const columns: ColumnDef<Org>[] = [
  {
    accessorKey: "name",
    header: "이름",
  },
  {
    accessorKey: "owner",
    header: "소유자",
  },
  {
    accessorKey: "dscription",
    header: "설명",
  },
  {
    id: "actions",
    cell: ({ row }) => {
      const payment = row.original;
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
            <DropdownMenuItem>상세보기</DropdownMenuItem>
            <DropdownMenuItem>편집</DropdownMenuItem>
            <DropdownMenuItem>삭제</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];
