"use client"
// 이걸 적는다고 CSR이 되는건 아님.
// 모든 component 는 우선적으로 SSR 되고
// use client 를 적는 것은 CSR 도 같이 이루어진다는 것을 뜻함

import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "../styles/nav.module.css"

export default function Nav() {
  const path = usePathname()

  return (
    <nav className={styles.nav}>
      <ul>
        <li>
          <Link href="/">Home</Link> 
          {path === "/" ? "🍕" : ""}
        </li>
        <li>
          <Link href="/about-us">about-us</Link> 
          {path === "/about-us" ? "🍕" : ""}
        </li>
      </ul>
    </nav>
  )
}