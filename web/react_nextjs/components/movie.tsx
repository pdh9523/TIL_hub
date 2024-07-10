"use client"

import Link from "next/link"
import styles from "../styles/movie.module.css"
import { useRouter } from "next/navigation"
interface IMovieProps {
  title: string
  id: string
  poster_path: string
}

export default function Movie({title, id, poster_path}: IMovieProps) {
  const router = useRouter()
  const onClick = () => {
    router.push(`/movies/${id}`)
  }
  return (
  <div key={id} className={styles.movie}>
    <img src={poster_path} alt={title} onClick={onClick}/>
    <Link prefetch href={`/movies/${id}`}>{title.length>15 ? title.slice(0,15) : title}</Link>
  </div>
  )
}