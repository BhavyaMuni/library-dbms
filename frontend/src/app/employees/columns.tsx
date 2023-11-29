"use client";

import { MoreHorizontal, Trash } from "lucide-react";
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
export type Employee = {
  employeeid: number;
  name: string;
  email: string;
  phone: string;
  address: string;
  hiredate: Date;
};

// function to post delete request to backend api
async function deleteEmployee(id: number) {
  const response = await fetch(`/api/employees/${id}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error("Failed to delete employee");
  }
}

export const columns: ColumnDef<Employee>[] = [
  {
    accessorKey: "employeeid",
    header: "ID",
  },
  {
    accessorKey: "name",
    header: "Name",
  },
  {
    accessorKey: "email",
    header: "Email",
  },
  {
    accessorKey: "phone",
    header: "Phone",
  },
  {
    accessorKey: "address",
    header: "Address",
  },
  {
    accessorKey: "hiredate",
    header: "Hire Date",
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
              onClick={() => deleteEmployee(row.original.employeeid)}
            >
              <Trash className="mr-2 h-4 w-4" />
              <span>Remove employee</span>
            </DropdownMenuItem>
            {/* <DropdownMenuItem
              onClick={() => updateEmployee(row.original.employeeid)}
            >
              <Trash className="mr-2 h-4 w-4" />
              <span>Update employee</span>
            </DropdownMenuItem> */}
          </DropdownMenuContent>
        </DropdownMenu>
      );
    },
  },
];
