import cProfile
import pstats
import io

def check_performance(path):
    """Check the performance of the code"""
    pr = cProfile.Profile()
    # run the code with profiling
    pr.run("check_syntax(path)")
    # create a stream to store the output
    s = io.StringIO()
    # create a profile stats object
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    # print the results
    ps.print_stats()
    # return the results
    return s.getvalue()
