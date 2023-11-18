import { Book, columns } from "./columns";
import { DataTable } from "./data-table";

const URL = "https://library-dbms-backend.vercel.app/api";

async function getBooks(): Promise<Book[]> {
  // Fetch data from your API here.
  const res = await fetch(`${URL}/books`);
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default async function BooksPage() {
  const data = await getBooks();

  return (
    <div className="container flex flex-col mx-auto justify-evenly h-auto">
      <h1 className="text-3xl font-bold py-4">Books</h1>
      <DataTable columns={columns} data={data} />
    </div>
  );
}
