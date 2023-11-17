"use client";

import { ColumnDef } from "@tanstack/react-table";

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Book = {
  title: string;
  author: string;
  publishedyear: number;
  totalstock: number;
  availablestock: number;
};

export const columns: ColumnDef<Book>[] = [
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
];
