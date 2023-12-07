"use client";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";

import * as z from "zod";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";
import { Plus } from "lucide-react";
import { DialogClose } from "@radix-ui/react-dialog";

const formSchema = z.object({
  bookid: z.coerce.number(),
  customerid: z.coerce.number(),
  employeeid: z.coerce.number(),
  checkoutdate: z.date(),
  duedate: z.date(),
  returndate: z.date().optional(),
  latefee: z.number().default(0),
});

export function CreateDialog() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      bookid: 0,
      customerid: 0,
      employeeid: 0,
      checkoutdate: new Date(),
      duedate: new Date(),
      returndate: undefined,
      latefee: 0,
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    values.checkoutdate = new Date();
    values.duedate = new Date(values.checkoutdate.getDate() + 30);
    const resp = await fetch(`/api/transactions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(values),
    });
    if (!resp.ok) {
      throw new Error("Failed to create transaction");
    }
  }
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="default" className="bg-green-600">
          <Plus className="mr-2 h-4 w-4" /> Create Transaction
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Create a new transaction</DialogTitle>
          <DialogDescription>
            Create a new transaction by filling out the form below.
          </DialogDescription>
        </DialogHeader>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
            <FormField
              control={form.control}
              name="bookid"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Book ID</FormLabel>
                  <FormControl>
                    <Input {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="customerid"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Customer ID</FormLabel>
                  <FormControl>
                    <Input {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="employeeid"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Employee ID</FormLabel>
                  <FormControl>
                    <Input {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <DialogFooter>
              <DialogClose asChild>
                <Button disabled type="submit">
                  Submit
                </Button>
              </DialogClose>
            </DialogFooter>
          </form>
        </Form>
      </DialogContent>
    </Dialog>
  );
}
