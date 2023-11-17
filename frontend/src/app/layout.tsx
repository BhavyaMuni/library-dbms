import type { Metadata } from "next";
import { Inter as FontSans } from "next/font/google";
import { MainNav } from "@/components/main-nav";
import { cn } from "@/lib/utils";
import "@/styles/globals.css";

export const fontSans = FontSans({
  subsets: ["latin-ext"],
  variable: "--font-sans",
});

export const metadata: Metadata = {
  title: "Library DBMS",
  description: "CPS510 - Group V18",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body
        className={cn(
          "min-h-screen bg-background font-sans antialiased",
          fontSans.variable
        )}
      >
        <MainNav className="mx-6" />
        {children}
      </body>
    </html>
  );
}
