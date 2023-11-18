import { Book, columns } from "./columns";
import { DataTable } from "./data-table";

const URL = "https://library-dbms-backend.vercel.app/api";
//   ? `https://${process.env.NEXT_PUBLIC_VERCEL_URL}/api`
//   : "http://localhost:3000/api";

async function getBooks(): Promise<Book[]> {
  // Fetch data from your API here.
  const res = await fetch(`${URL}/books`, { cache: "no-store" });
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function BooksPage() {
  const data = await getBooks();

  return (
    <div className="container mx-auto py-10">
      <DataTable columns={columns} data={data} />
    </div>
  );
}
