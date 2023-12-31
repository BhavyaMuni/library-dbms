"use client";

import { Employee, columns } from "./columns";
import { DataTable } from "./data-table";

import { useEffect, useState } from "react";

async function getEmployees(): Promise<Employee[]> {
  // Fetch data from your API here.
  const res = await fetch(`/api/employees`);
  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }
  return res.json();
}

export default function EmployeesPage() {
  //   const data = await getEmployees();

  const [data, setData] = useState<Employee[]>([]);

  useEffect(() => {
    getEmployees().then((data) => setData(data));
  }, []);

  const updateEmployees = (new_data: Employee[]) => {
    setData(new_data);
  };

  return (
    <div className="container flex flex-col mx-auto justify-evenly h-auto">
      <h1 className="text-3xl font-bold py-4">Employees</h1>
      <DataTable
        columns={columns}
        data={data}
        updateFunction={updateEmployees}
      />
    </div>
  );
}
