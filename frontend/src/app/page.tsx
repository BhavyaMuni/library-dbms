"use client";

import { Button } from "@/components/ui/button";
import { Transaction, columns } from "./columns";
import { DataTable } from "./data-table";
import { CreateDialog } from "./dialog-create";
import { Input } from "@/components/ui/input";
import { useEffect, useState } from "react";

async function getTransactions(): Promise<Transaction[]> {
  // Fetch data from your API here.
  const res = await fetch(`/api/transactions`);
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default function TransactionsPage() {
  //   const data = await getTransactions();

  const [data, setData] = useState<Transaction[]>([]);

  useEffect(() => {
    getTransactions().then((data) => setData(data));
  }, []);

  const updateTransactions = (new_data: Transaction[]) => {
    setData(new_data);
  };

  return (
    <div className="container flex flex-col mx-auto justify-evenly h-auto">
      <h1 className="text-3xl font-bold py-4">Transactions</h1>
      <DataTable
        columns={columns}
        data={data}
        updateFunction={updateTransactions}
      />
    </div>
  );
}
