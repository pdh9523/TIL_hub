import { Key } from "react"
import Movie, {IMovieProps} from "../../components/movie"
import styles from ".//web/react_nextjs/styles/home.module.css"
import {API_URL} from "../constants"


export const metadata = {
  title: "home",
}

async function getMovies() {
  await new Promise((resolve) => setTimeout(resolve, 1000))
  const response = await fetch(API_URL)
  return await response.json()
}

// function 이름은 별로 상관 없음
export default async function Page() {
  const movies = await getMovies()

  return <div className={styles.container}>
    {movies.map((movie: IMovieProps) =>
    <Movie
      key={movie.id}
      id={movie.id}
      title={movie.title}
      poster_path={movie.poster_path}
    />
  )}

</div>
}