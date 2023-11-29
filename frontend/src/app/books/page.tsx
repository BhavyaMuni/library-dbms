"use client";

import { Button } from "@/components/ui/button";
import { Book, columns } from "./columns";
import { DataTable } from "./data-table";
import { CreateDialog } from "./dialog-create";
import { Input } from "@/components/ui/input";
import { useEffect, useState } from "react";

async function getBooks(): Promise<Book[]> {
  // Fetch data from your API here.
  const res = await fetch(`/api/books`);
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default function BooksPage() {
  //   const data = await getBooks();

  const [data, setData] = useState<Book[]>([]);

  useEffect(() => {
    getBooks().then((data) => setData(data));
  }, []);

  const updateBooks = (new_data: Book[]) => {
    setData(new_data);
  };

  return (
    <div className="container flex flex-col mx-auto justify-evenly h-auto">
      <h1 className="text-3xl font-bold py-4">Books</h1>
      <DataTable columns={columns} data={data} updateFunction={updateBooks} />
    </div>
  );
}
