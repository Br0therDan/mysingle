// @/components/dashboard/data-table
"use client";
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
  flexRender,
} from "@tanstack/react-table";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { File, PlusCircle, Settings } from "lucide-react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import Link from "next/link";
import React from "react";
import { useTranslations } from "next-intl";
import { capitalizeFirstLetter } from '@/lib/utils';

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[];
  data: TData[];
  title: string;
  description?: string;
}

export default function DataTableLegacy<TData, TValue>({
  columns,
  data,
  title,
  description,
}: DataTableProps<TData, TValue>) {
  const [sorting, setSorting] = React.useState<SortingState>([]);
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  );
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({});

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onColumnFiltersChange: setColumnFilters,
    onSortingChange: setSorting,
    getSortedRowModel: getSortedRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
    },
  });
  const t = useTranslations(`tableHeaders`); // i18n 훅 사용

  return (
    <div className="flex flex-col gap-2 w-auto">
      <TableMenu columns={columns} table={table} title={title} />
      <Card>
        <CardHeader>
          <CardTitle>{t(`${title}.table_name`)}</CardTitle>
          <CardDescription>
            <div className="flex items-center justify-between gap-2">
              <div>{description}</div>
            </div>
          </CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              {table.getHeaderGroups().map((headerGroup) => (
                <TableRow key={headerGroup.id}>
                  {headerGroup.headers.map((header) => {
                    return (
                      <TableHead key={header.id}>
                        {header.isPlaceholder
                          ? null
                          : flexRender(
                              typeof header.column.columnDef.header === "string"
                                ? t(
                                    `${title}.` + header.column.columnDef.header
                                  ) // 헤더 텍스트를 번역된 텍스트로 대체
                                : header.column.columnDef.header,
                              header.getContext()
                            )}
                      </TableHead>
                    );
                  })}
                </TableRow>
              ))}
            </TableHeader>
            <TableBody>
              {table.getRowModel().rows?.length ? (
                table.getRowModel().rows.map((row) => (
                  <TableRow
                    key={row.id}
                    data-state={row.getIsSelected() && "selected"}
                  >
                    {row.getVisibleCells().map((cell) => (
                      <TableCell key={cell.id}>
                        {flexRender(
                          cell.column.columnDef.cell,
                          cell.getContext()
                        )}
                      </TableCell>
                    ))}
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell
                    colSpan={columns.length}
                    className="h-24 text-center"
                  >
                    No results.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}

function TableMenu<TData, TValue>({
  columns,
  table,
  title
}: {
  columns: ColumnDef<TData, TValue>[];
  table: ReturnType<typeof useReactTable<TData>>;
  title: string;
}) {
  const t = useTranslations(); 
  return (
    <div className="flex justify-end items-center gap-2">
      <DropdownMenu>
        <DropdownMenuTrigger asChild>
          <Button size="sm" variant="outline" className="h-8 gap-1">
            <Settings className="h-3.5 w-3.5" />
          {t("button.columns")}
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end">
          {table
            .getAllColumns()
            .filter((column) => column.getCanHide())
            .map((column) => {
              return (
                <DropdownMenuCheckboxItem
                  key={column.id}
                  className="capitalize"
                  checked={column.getIsVisible()}
                  onCheckedChange={(value) => column.toggleVisibility(!!value)}
                >
                  {column.id}
                </DropdownMenuCheckboxItem>
              );
            })}
        </DropdownMenuContent>
      </DropdownMenu>
      <Button variant="outline" className="h-8 gap-1">
        <File className="h-3.5 w-3.5" />
        {t("button.export")}
      </Button>
      <Link href={`/${title}s/register`}>
        <Button className="h-8 gap-1">
          <PlusCircle className="h-3.5 w-3.5" />
          <span className="sr-only sm:not-sr-only sm:whitespace-nowrap">
          {t(`button.create${capitalizeFirstLetter(title)}`)}
          </span>
        </Button>
      </Link>
    </div>
  );
}
