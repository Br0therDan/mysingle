import { Search } from "lucide-react";
import React from "react";
import { Input } from "@/components/ui/input";

export default function SearchBar() {
  return (
    <div className="relative ml-auto flex-1 md:grow-0">
      <Search className="absolute left-2.5 top-2 h-4 w-4 text-muted-foreground" />
      <Input
        type="search"
        placeholder="Search..."
        className="h-8 w-full rounded-lg bg-background pl-8 md:w-[200px] lg:w-[336px]"
      />
    </div>
  );
}
