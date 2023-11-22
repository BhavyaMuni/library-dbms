"use client";

import { MoreHorizontal } from "lucide-react";
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

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Book = {
  bookid: number;
  title: string;
  author: string;
  publishedyear: number;
  totalstock: number;
  availablestock: number;
};

// function to post delete request to backend api
async function deleteBook(id: number) {
  const response = await fetch(`/api/books/${id}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error("Failed to delete book");
  }
}

export const columns: ColumnDef<Book>[] = [
  {
    accessorKey: "bookid",
    header: "ID",
  },
  {
    accessorKey: "title",
    header: "Title",
  },
  {
    accessorKey: "author",
    header: "Author",
  },
  {
    accessorKey: "publishedyear",
    header: "Published Year",
  },
  {
    accessorKey: "totalstock",
    header: "Total Stock",
  },
  {
    accessorKey: "availablestock",
    header: "Available Stock",
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const book = row.original;

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
            <Button
              variant="destructive"
              onClick={() => deleteBook(book.bookid)}
            >
              Delete Book
            </Button>
            <DropdownMenuSeparator />
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];
