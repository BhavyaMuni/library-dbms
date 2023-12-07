"use client";

import { CalendarIcon, MoreHorizontal, Trash } from "lucide-react";
import { ColumnDef } from "@tanstack/react-table";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { cn } from "@/lib/utils";
import { format } from "date-fns";
import React from "react";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Transaction = {
  transactionid: number;
  bookid: number;
  customerid: number;
  employeeid: number;
  checkoutdate: string;
  duedate: string;
  returndate: Date | undefined;
  latefee: number | 0;
};

// function to post delete request to backend api
async function deleteTransaction(id: number) {
  const response = await fetch(`/api/transactions/${id}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error("Failed to delete transaction");
  }
}

async function getBook(id: number): Promise<string> {
  const response = await fetch(`/api/books/${id}`);
  if (!response.ok) {
    throw new Error("Failed to fetch book");
  }
  const data = await response.json();
  return data.title;
}

export const columns: ColumnDef<Transaction>[] = [
  {
    accessorKey: "transactionid",
    header: "ID",
  },
  {
    accessorKey: "bookid",
    header: "Book",
    cell: ({ row }) => {
      const [book, setBook] = React.useState<string>("");

      React.useEffect(() => {
        getBook(row.original.bookid).then((data) => setBook(data));
      }, []);

      return book;
    },
  },
  {
    accessorKey: "customerid",
    header: "Customer",
  },
  {
    accessorKey: "employeeid",
    header: "Employee",
  },
  {
    accessorKey: "checkoutdate",
    header: "Checkout",
    cell: ({ row }) => {
      return (
        <Button
          disabled
          variant={"ghost"}
          className={cn(
            "w-[280px] justify-start text-left font-normal",
            !row.original.checkoutdate && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {format(Date.parse(row.original.checkoutdate), "PPP")}
        </Button>
      );
    },
  },
  {
    accessorKey: "duedate",
    header: "Due Date",
    cell: ({ row }) => {
      return (
        <Button
          disabled
          variant={"ghost"}
          className={cn(
            "w-[280px] justify-start text-left font-normal",
            !row.original.duedate && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {format(Date.parse(row.original.duedate), "PPP")}
        </Button>
      );
    },
  },
  {
    accessorKey: "latefee",
    header: "Late Fee",
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      return (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="h-8 w-8 p-0">
              <span className="sr-only">Open menu</span>
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuLabel>Actions</DropdownMenuLabel>
            <DropdownMenuItem
              disabled
              onClick={() => deleteTransaction(row.original.transactionid)}
            >
              <Trash className="mr-2 h-4 w-4" />
              <span>Delete transaction</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];
