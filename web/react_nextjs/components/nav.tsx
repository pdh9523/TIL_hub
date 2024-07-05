// 이걸 적는다고 CSR이 되는건 아님.
// 모든 component 는 우선적으로 SSR 되고
// use client 를 적는 것은 CSR 도 같이 이루어진다는 것을 뜻함
"use client"

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

export default function Nav() {
  const path = usePathname()
  const [count, setCount] = useState(0)

  return (
    <nav>
      <ul>
        <li>
          <Link href="/">Home</Link> {path === "/" ? "🍕" : ""}
        </li>
        <li>
          <Link href="/about-us">about-us</Link> {path === "/about-us" ? "🍕" : ""}
        </li>
        <li>
          <button onClick={() => setCount((c)=>c+1)}>{count}</button>
        </li>
      </ul>
    </nav>
  )
}