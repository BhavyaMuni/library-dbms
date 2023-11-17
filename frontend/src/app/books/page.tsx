import { Book, columns } from "./columns";
import { DataTable } from "./data-table";

async function getBooks(): Promise<Book[]> {
  // Fetch data from your API here.
  const res = await fetch("/api/books");
  const data = await res.json();
  return data;
  return [
    // ...
  ];
}

export default async function DemoPage() {
  const data = await getBooks();

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  );
}
