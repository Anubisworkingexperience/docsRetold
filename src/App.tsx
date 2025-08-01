import { ChatInterface } from "./components/ChatInterface"
import { AnswerSection } from "./components/AnswerSection";
import './styles/app.module.css'
import styles from './styles/app.module.css';

function App() {

  return (
    <>
      <div className={styles.app}>
        <h1>DocsRetold</h1>
        <p>Send a text to summarize</p>
        <AnswerSection />
        <ChatInterface />
      </div>
    </>
  )
}

export default App
