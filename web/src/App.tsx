import { HashRouter, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Home from './pages/Home'
import Leaderboard from './pages/Leaderboard'
import Rules from './pages/Rules'
import Submit from './pages/Submit'
import Submission from './pages/Submission'

export default function App() {
  return (
    <HashRouter>
      <div className="min-h-screen flex flex-col">
        <Navbar />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/rules" element={<Rules />} />
            <Route path="/submit" element={<Submit />} />
            <Route path="/submission/:id" element={<Submission />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </HashRouter>
  )
}
