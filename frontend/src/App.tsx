import {motion} from "motion/react"
import GainersList from "./components/TopGainers";
import LosersList from "./components/TopLosers";


function App() {
  return (
    <div className="h-screen w-full bg-gradient-to-br from-[#0E0E10] via-[#1F2937] to-[#14B8A6] overflow-hidden">
      <motion.div
        className="bg-[#1F2937] opacity-50 w-[90vw] h-[40vh] rounded-[25px] relative items-center justify-center top-[5vh] left-[5vw] overflow-y-auto scrollbar-hide flex flex-col"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        <motion.div
          className="text-white text-2xl font-bold text-center mt-4 relative top-[-18vh]"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
        >
        
        </motion.div>
        <motion.div
          className="text-white text-2xl font-bold text-center mt-4 relative top-[-18vh]  "
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
        >
          <div className="overflow-auto scrollbar-hide bg-[#1F2937] w-[90vw] h-[40vh] rounded-[25px] relative items-center justify-center top-[17vh] left-[0vw] opacity-75 z-[1]">
            <GainersList />
          </div>
          
          
        </motion.div>

      </motion.div>
      <motion.div
        className="bg-[#1F2937] opacity-50 w-[90vw] h-[40vh] rounded-[25px] relative items-center justify-center top-[15vh] left-[5vw] overflow-y-auto scrollbar-hide flex flex-col"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
      
        <motion.div
          className="text-white text-2xl font-bold text-center mt-4 relative top-[-18vh]"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
        >
          
        </motion.div>
        <motion.div
          className="text-white text-2xl font-bold text-center mt-4 relative top-[-18vh]"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
        >

          <div className="overflow-auto scrollbar-hide bg-[#1F2937] w-[90vw] h-[40vh] rounded-[25px] relative items-center justify-center top-[17vh] left-[0vw] opacity-75 z-[1]">
            <LosersList />
          </div>
          
        </motion.div>    

      </motion.div>

   
      
    </div>

      
        
      
      
  );
}

export default App;