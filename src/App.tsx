import { ChatInterface } from "./components/ChatInterface"
import './styles/app.module.css'
import styles from './styles/app.module.css';

function App() {

  return (
    <>
      <div className={styles.app}>
        <h1>DocsRetold</h1>
        <p>Send a text to summarize</p>
        <ChatInterface />
      </div>
    </>
  )
}

export default App
