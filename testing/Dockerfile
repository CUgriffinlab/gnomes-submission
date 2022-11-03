# Install python
FROM python:3.9

# Install dragg
RUN pip install dragg==1.2.3rc0 #--pre

# Install dragg-comp
RUN pip install dragg-comp==0.2.2rc0 #--pre
RUN pip install cvxopt

# Copy parent directory
ADD . /dragg-comp-submission

# Install submission
RUN pip install /dragg-comp-submission/.

# Run Tests
CMD python /dragg-comp-submission/testing/test_submission.py
