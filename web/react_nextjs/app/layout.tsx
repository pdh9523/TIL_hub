import { Metadata } from "next"
import Nav from "../components/nav"
import "../styles/global.css"

export const metadata: Metadata = {
  title: {
    template: "%s | Next Movies",
    default: "Next Movies"
  }
}

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="ko">
      <body>
        <Nav />
        {children}
      </body>
    </html>
  )
}