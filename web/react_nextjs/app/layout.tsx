import { Metadata } from "next"
import Nav from "../components/nav"

export const metadata: Metadata = {
  title: {
    template: "%s | Next Movies",
    default: "Loading..."
  }
}

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="ko">
      <body>
        <Nav />
        <h6>I'm Layout</h6>
        {children}
      </body>
    </html>
  )
}
