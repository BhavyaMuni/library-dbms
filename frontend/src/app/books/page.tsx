import { Book, columns } from "./columns";
import { DataTable } from "./data-table";

const URL = process.env.NEXT_PUBLIC_VERCEL_URL
  ? `https://${process.env.NEXT_PUBLIC_VERCEL_URL}/api`
  : "http://localhost:8000/api";

async function getBooks(): Promise<Book[]> {
  // Fetch data from your API here.
  const res = await fetch(`${URL}/books`);
  console.log(res);
  const data = await res.json();
  return data;
}

export default async function DemoPage() {
  const data = await getBooks();

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  );
}
