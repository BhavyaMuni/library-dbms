"use client";

import { Customer, columns } from "./columns";
import { DataTable } from "./data-table";

import { useEffect, useState } from "react";

async function getCustomers(): Promise<Customer[]> {
  // Fetch data from your API here.
  const res = await fetch(`/api/customers`);
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default function CustomersPage() {
  //   const data = await getCustomers();

  const [data, setData] = useState<Customer[]>([]);

  useEffect(() => {
    getCustomers().then((data) => setData(data));
  }, []);

  const updateCustomers = (new_data: Customer[]) => {
    setData(new_data);
  };

  return (
    <div className="container flex flex-col mx-auto justify-evenly h-auto">
      <h1 className="text-3xl font-bold py-4">Customers</h1>
      <DataTable
        columns={columns}
        data={data}
        updateFunction={updateCustomers}
      />
    </div>
  );
}
