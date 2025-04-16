function App() {
  return (
    <div className="h-screen w-full bg-gradient-to-br from-[#0E0E10] via-[#1F2937] to-[#14B8A6] overflow-hidden">
      <div className="flex flex-col items-center justify-center h-full w-full relative text-white">
        <h1 className="text-4xl font-bold mb-4 absolute top-[15%]">TOP BUY</h1>
        <div className="bg-[#1F2937] opacity-50 relative ">
          <p
            className="absolute  bg-[#1F2937]
            w-[340px] h-[200px] top-[50%] left-[50%] translate-x-[-50%] translate-y-[-100%]
            sm:w-[100px] sm:h-[400px] sm:top-[50%] sm:left-[50%] sm:translate-x-[-50%] sm:translate-y-[-215%]
            md:w-[500px] md:h-[320px] "
          >
            {/* Add content here */}
          </p>
        </div>
      </div>
    </div>
  );
}

export default App;