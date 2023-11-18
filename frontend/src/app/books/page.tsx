import { Book, columns } from "./columns";
import { DataTable } from "./data-table";

const URL = process.env.BACKEND_URL
  ? `https://${process.env.BACKEND_URL}/api`
  : "http://localhost:8000/api";

async function getBooks(): Promise<Book[]> {
  // Fetch data from your API here.
  const res = await fetch(`${URL}/books`);
  return await res.json();
}

export default async function DemoPage() {
  const data = await getBooks();

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  );
}
