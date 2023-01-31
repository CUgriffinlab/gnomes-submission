# Install python
FROM python:3.9

# Copy parent directory
ADD . /dragg-comp-submission

# Install submission
RUN pip install /dragg-comp-submission/.

# Run Tests
CMD python /dragg-comp-submission/testing/test_submission.py
