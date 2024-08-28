import { ColumnDef } from "@tanstack/react-table";
import { Button } from "@/components/ui/button";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { MoreHorizontal } from "lucide-react";
import { formatInTimeZone } from "date-fns-tz";
import Link from "next/link";
import { entityConfigMap } from "@/config/entities";
import { BaseEntityConfig } from '@/types/base';


// generateColumns 함수에서 TData는 각 엔티티 타입이 됩니다.
export function generateColumns<TData extends { [key: string]: any }>(
  entity: keyof typeof entityConfigMap
): ColumnDef<TData>[] {
  const config: BaseEntityConfig = entityConfigMap[entity];

  const columns: ColumnDef<TData>[] = Object.keys(config.fields).map((field) => {
    const fieldConfig = config.fields[field];

    if (!fieldConfig.showInTable) return null; // 테이블에 표시하지 않을 필드 필터링

    return {
      accessorKey: field,
      header: fieldConfig.label,
      cell: ({ row }: { row: { original: TData; getValue: (key: string) => unknown } }) => {
        const value = row.getValue(field);
        
        if (fieldConfig.type === "string" && fieldConfig.options) {
          return fieldConfig.options.includes(value as string) ? value : "-";
        } else if (fieldConfig.type === "date") {
          const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
          const date = new Date(value as string);
          return formatInTimeZone(date, userTimeZone, "yyyy-MM-dd HH:mm");
        } else if (fieldConfig.type === "link") {
          const id = row.original[config.identifierKey as keyof TData];
          const linkTemplate = fieldConfig.linkTemplate ? fieldConfig.linkTemplate : `/${entity}/${id}`;
          const link = linkTemplate.replace("{id}", String(id));
          return (
            <Link href={link} className="text-blue-600 hover:underline">
              {value as string}
            </Link>
          );
        } else {
          return String(value);
        }
      },
    };
  }).filter(Boolean) as ColumnDef<TData>[];

  columns.push({
    id: "actions",
    cell: ({ row }) => {
      const item = row.original;
      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only">Open menu</span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem asChild>
              <Link href={`/${entity}/${item[config.identifierKey as keyof TData]}`}>
                Detail
              </Link>
            </DropdownMenuItem>
            <DropdownMenuItem asChild>
              <Link href={`/${entity}/edit/${item[config.identifierKey as keyof TData]}`}>
                Edit
              </Link>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  });

  return columns;
}
