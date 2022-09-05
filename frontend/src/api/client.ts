import {
  ApolloClient,
  ApolloLink,
  concat,
  createHttpLink,
  DefaultOptions,
  InMemoryCache,
} from "@apollo/client/core";
import { useAuthStore } from "../store/auth";

const httpLink = createHttpLink({
  uri: import.meta.env.VITE_GRAPHQL_API_URL,
  credentials: "same-origin",
});

const authMiddleware = new ApolloLink((operation, forward) => {
  const token = useAuthStore().getAuthToken;
  operation.setContext({
    headers: {
      authorization: token ? `Bearer ${token}` : "",
    },
  });
  return forward(operation);
});

const defaultOptions: DefaultOptions = {
  watchQuery: {
    fetchPolicy: "no-cache",
    errorPolicy: "ignore",
  },
  query: {
    fetchPolicy: "no-cache",
    errorPolicy: "all",
  },
};

const cache = new InMemoryCache();

export const apolloClient = new ApolloClient({
  link: concat(authMiddleware, httpLink),
  cache,
  defaultOptions,
});
